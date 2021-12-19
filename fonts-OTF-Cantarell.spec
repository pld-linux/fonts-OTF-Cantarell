Summary:	Cantarell fonts
Summary(pl.UTF-8):	Fonty Cantarell
Name:		fonts-OTF-Cantarell
Version:	0.303.1
Release:	1
License:	OFL v1.1
Group:		Fonts
Source0:	https://download.gnome.org/sources/cantarell-fonts/0.303/cantarell-fonts-%{version}.tar.xz
# Source0-md5:	a9be59ddb29204dcfd3357f201949b8c
URL:		https://gitlab.gnome.org/GNOME/cantarell-fonts/
BuildRequires:	gettext-its-metainfo
BuildRequires:	gettext-tools
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	psautohint >= 2.0.0
BuildRequires:	python3-attrs >= 18.2
BuildRequires:	python3-cffsubr >= 0.2.8
BuildRequires:	python3-fontMath >= 0.5.0
# fontTools[ufo,lxml,unicode]
BuildRequires:	python3-fonttools >= 4.0.0
BuildRequires:	python3-lxml >= 4
BuildRequires:	python3-skia-pathops
BuildRequires:	python3-statmake >= 0.1.3
# ufo2ft[cffsubr]
BuildRequires:	python3-ufo2ft >= 2.15.0
BuildRequires:	python3-ufoLib2 >= 0.4.0
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	fontpostinst
Requires:	fontconfig >= 1:2.10.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_otffontsdir	%{_fontsdir}/OTF

%description
Cantarell is a set of fonts originally designed by Dave Crossland. It
is a sans-serif Humanist typeface family.

%description -l pl.UTF-8
Cantarell to zbiór fontów pierwotnie zaprojektowanych przez Dave'a
Crosslanda. Jest to rodzina krojów bezszeryfowych Humanist.

%prep
%setup -q -n cantarell-fonts-%{version}

%build
%meson build \
	-Dfontsdir=%{_otffontsdir}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst OTF

%postun
fontpostinst OTF

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README.md
%{_otffontsdir}/Cantarell-*.otf
%{_datadir}/metainfo/org.gnome.cantarell.metainfo.xml
