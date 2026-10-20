FROM debian:trixie
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates git curl wget make g++ pkg-config cmake autoconf automake \
    libtool dpkg-dev fontforge poppler-utils libpng-dev zlib1g-dev \
    libfreetype6-dev libjpeg-dev libopenjp2-7-dev libxml2-dev libglib2.0-dev gettext jq \
    python3 openjdk-21-jdk-headless && rm -rf /var/lib/apt/lists/*

WORKDIR /src
COPY . /src
# The upstream build scripts are designed for interactive Debian hosts and
# invoke sudo. In the build container they already run as root.
RUN find buildScripts -type f -exec sed -i 's/sudo //g' {} + \
    && sed -i '/openjdk-17-jre-headless/d' buildScripts/getBuildToolsApt \
    && python3 -c 'p="buildScripts/getFontforge"; s=open(p).read(); needle="mv fontforge-$FONTFORGE_VERSION fontforge"; s=s.replace(needle, needle + "\nsed -i s/--check//g fontforge/po/CMakeLists.txt"); open(p,"w").write(s)' \
    && export CFLAGS="$(pkg-config --cflags glib-2.0 gio-2.0 gobject-2.0)" \
    && export CXXFLAGS="$CFLAGS" \
    && ./buildScripts/buildInstallLocallyApt

WORKDIR /work
ENTRYPOINT ["pdf2htmlEX"]

