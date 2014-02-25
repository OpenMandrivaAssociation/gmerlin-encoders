######################
# Hardcode PLF build
%define build_plf 0
######################

%if %{build_plf}
%define distsuffix plf
%define extrarelsuffix plf
%endif

Summary:	A multimedia encoding library
Name:		gmerlin-encoders
Version:	1.2.0
Release:	1%{?extrarelsuffix}
License:	LGPLv2+
Group:		Video
Url:		http://gmerlin.sourceforge.net/
Source0:	http://downloads.sourceforge.net/gmerlin/%{name}-%{version}.tar.gz
Patch0:		gmerlin-encoders-1.2.0-ffmpeg2.patch
BuildRequires:	gmerlin
BuildRequires:	ffmpeg-devel
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(gavl)
BuildRequires:	pkgconfig(gmerlin)
BuildRequires:	pkgconfig(mjpegtools)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(shout)
BuildRequires:	pkgconfig(speex)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(vorbis)
%if %{build_plf}
BuildRequires:	libfaac-devel
BuildRequires:	lame-devel
%endif

%description
This package contains some encoder plugins for gmerlin.
If you install it, gmerlin-transcoder will be able to
encode more file formats.

%files -f %{name}.lang
%{_libdir}/gmerlin/plugins/*.so

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
make

%install
%makeinstall_std

%find_lang %{name}

