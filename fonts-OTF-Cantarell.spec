Summary:	Cantarell fonts
Summary(pl.UTF-8):	Fonty Cantarell
Name:		fonts-OTF-Cantarell
Version:	0.201
Release:	1
License:	OFL v1.1
Group:		Fonts
Source0:	http://ftp.gnome.org/pub/GNOME/sources/cantarell-fonts/%{version}/cantarell-fonts-%{version}.tar.xz
# Source0-md5:	8f47a0e6bb76b6bb816ef61d4f80ec8a
URL:		https://gitlab.gnome.org/GNOME/cantarell-fonts/
BuildRequires:	gettext-its-metainfo
BuildRequires:	gettext-tools
BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.727
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

%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

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
