Name:           noson-app
Version:        3.9.7
Release:        1
Summary:        SONOS device controller
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            http://janbar.github.io/noson-app/index.html
Source0:        https://github.com/janbar/noson-app/archive/%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(noson) >= 1.16.2

%description
A controller for SONOS devices. It allows for browsing the music
library, and playing tracks or radio on any zones. Zone groups,
queues and playlists can be managed, and playback be controlled.

%prep
%setup -q -n %{name}-%{version}/noson-app

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_DEPENDENCIES=OFF \
    -DBUILD_LIBNOSON=OFF \
    -DBUILD_SAILFISHOS=ON
make

%install
%make_install -C build

%files
%{_bindir}/noson-app
%{_datadir}/applications/io.github.janbar.noson.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/metainfo/io.github.janbar.noson.appdata.xml
%{_libdir}/noson/

%changelog
