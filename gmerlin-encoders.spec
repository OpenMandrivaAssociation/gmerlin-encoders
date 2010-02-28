%define build_plf 0
%{?_with_plf: %{expand: %%global build_plf 1}}

%if %build_plf
%define distsuffix plf
%endif

Name: gmerlin-encoders
Summary: A multimedia encoding library
Version: 0.2.9
Release: %mkrel 1
Url: http://gmerlin.sourceforge.net/
License: LGPLv2+
Group: Video
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Source0: http://downloads.sourceforge.net/gmerlin/%name-%version.tar.gz
BuildRequires: gavl-devel >= 1.1.2
BuildRequires: gmerlin-devel >= 0.4.2
BuildRequires: gmerlin >= 0.4.2
BuildRequires: ffmpeg-devel
BuildRequires: libogg-devel
BuildRequires: libflac-devel
BuildRequires: libmjpegtools-devel
BuildRequires: libshout-devel
BuildRequires: speex-devel
BuildRequires: libtheora-devel
BuildRequires: libvorbis-devel
%if %build_plf
BuildRequires: libfaac-devel
BuildRequires: lame-devel
%endif
BuildRequires: gettext

%description
This package contains some encoder plugins for gmerlin.
If you install it, gmerlin-transcoder will be able to
encode more file formats.

%files -f %name.lang
%defattr(-,root,root)
%_libdir/gmerlin/plugins/*.so

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std

rm -f %buildroot%_libdir/gmerlin/plugins/*.la

%find_lang %name

%clean
rm -rf %buildroot
