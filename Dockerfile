FROM fedora

RUN dnf install gcc rpm-build rpm-devel rpmlint make python bash coreutils diffutils patch rpmdevtools python3-devel which -y

RUN rpmdev-setuptree

VOLUME /code
WORKDIR /code
