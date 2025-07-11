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

if [ "$TARGET" != "local" ]; then
    if [ -z "$BUCKET_NAME" ] || [ -z "$BUCKET_PATH" ]; then
        echo "Error: BUCKET_NAME and BUCKET_PATH environment variables must be set"
        exit 1
    fi
fi

# Only show interactive prompt if not running in CI/automated environment
if [ -z "$CI" ] && [ -z "$GITHUB_ACTIONS" ]; then
    read -p "Press ENTER to deploy $VERSION_FILE and $LATEST_FILE to environment $TARGET (s3://$BUCKET_NAME/$BUCKET_PATH/)"
fi

case "$TARGET" in
	dev | staging | prod)
		echo "Uploading version file $VERSION_FILE to s3://$BUCKET_NAME/$BUCKET_PATH/"
		aws s3 cp "$VERSION_FILE" "s3://$BUCKET_NAME/$BUCKET_PATH/"
		echo "Uploading $LATEST_FILE to s3://$BUCKET_NAME/$BUCKET_PATH/"
		aws s3 cp "$LATEST_FILE" "s3://$BUCKET_NAME/$BUCKET_PATH/"
		;;
	local)
		echo "Listing contents of minio-local:/saas/vspeclib to verify rclone is here and connection works..."
		rclone ls minio-local:saas/vspeclib
		echo "Uploading version file $VERSION_FILE to minio-local:/saas/vspeclib/"
		rclone copy "$VERSION_FILE" minio-local:/saas/vspeclib/
		echo "Uploading $LATEST_FILE to minio-local:/saas/vspeclib/"
		rclone copy "$LATEST_FILE" minio-local:/saas/vspeclib/
		;;
	*)
		echo "Unknown target environment: $TARGET"
		exit 1
esac

echo "Deployment completed successfully!"
echo "Files uploaded to: s3://$BUCKET_NAME/$BUCKET_PATH/"
