#!/usr/bin/env bash
set -e

if [ -z "$1" ]; then
	echo "Must specify one of 'dev', 'internal', 'staging', 'production', or 'local' as a target for the deployment of the V spec library"
	exit 1
fi
LATEST_FILE="vspec_library.latest"
TARGET="$1"
VERSION=$(cat $LATEST_FILE)
VERSION_FILE=""vspec_library_$VERSION.json""

read -p "Press ENTER to deploy $VERSION_FILE and $LATEST_FILE to environment $TARGET"

case "$TARGET" in
	dev | internal | staging | production)
		echo "Uploading version file $VERSION_FILE to s3://veridise-$TARGET/vspeclib/"
		aws s3 cp "$VERSION_FILE" "s3://veridise-$TARGET/vspeclib/"
		echo "Uploading $LATEST_FILE to s3://veridise-$TARGET/vspeclib/"
		aws s3 cp "$LATEST_FILE" "s3://veridise-$TARGET/vspeclib/"
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
		echo Unknown target environment: $TARGET
		exit 1
esac
echo "Done"
