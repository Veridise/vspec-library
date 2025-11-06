#!/usr/bin/env bash
set -e
if [ -z "$1" ]; then
	echo "Must specify one of 'dev', 'staging', 'prod', or 'local' as a target for the deployment of the V spec library"
	exit 1
fi

LATEST_FILE="vspec_library.latest"
TARGET="$1"
VERSION=$(cat $LATEST_FILE)
VERSION_FILE="vspec_library_$VERSION.json"
BUCKET_PATH="${BUCKET_PATH:-vspeclib}"
OBJECT_STORAGE_CONF="s3"

if [ "$TARGET" != "local" ]; then
    if [ -z "$BUCKET_NAME" ] || [ -z "$BUCKET_PATH" ]; then
        echo "Error: BUCKET_NAME and BUCKET_PATH environment variables must be set"
        exit 1
    fi
	object_storage_full_path="$OBJECT_STORAGE_CONF://$BUCKET_NAME/$BUCKET_PATH/"
else
	BUCKET_NAME="saas"
	OBJECT_STORAGE_CONF="MINIO"
	export RCLONE_CONFIG_MINIO_TYPE="s3"
	export RCLONE_CONFIG_MINIO_PROVIDER="Minio"
	export RCLONE_CONFIG_MINIO_ACCESS_KEY_ID="root"
	export RCLONE_CONFIG_MINIO_SECRET_ACCESS_KEY="root-pass"
	export RCLONE_CONFIG_MINIO_ENDPOINT="https://minio-api.local.veridise.tools"
	object_storage_full_path="$OBJECT_STORAGE_CONF://$BUCKET_NAME/$BUCKET_PATH/"
fi

# Only show interactive prompt if not running in CI/automated environment
if [ -z "$CI" ] && [ -z "$GITHUB_ACTIONS" ]; then
    read -p "Press ENTER to deploy $VERSION_FILE and $LATEST_FILE to environment $TARGET ($object_storage_full_path)"
fi

case "$TARGET" in
	dev | staging | prod)
		echo "Uploading version file $VERSION_FILE to $object_storage_full_path"
		aws s3 cp "$VERSION_FILE" "$object_storage_full_path"
		echo "Uploading $LATEST_FILE to $object_storage_full_path"
		aws s3 cp "$LATEST_FILE" "$object_storage_full_path"
		;;
	local)
		echo "Listing contents of $object_storage_full_path to verify rclone is here and connection works..."
		rclone ls $object_storage_full_path --no-check-certificate
		echo "Uploading version file $VERSION_FILE to $object_storage_full_path"
		rclone copy "$VERSION_FILE" $object_storage_full_path --no-check-certificate
		echo "Uploading $LATEST_FILE to $object_storage_full_path"
		rclone copy "$LATEST_FILE" $object_storage_full_path --no-check-certificate
		;;
	*)
		echo "Unknown target environment: $TARGET"
		exit 1
esac

echo "Deployment completed successfully!"
echo "Files uploaded to: s3://$BUCKET_NAME/$BUCKET_PATH/"
