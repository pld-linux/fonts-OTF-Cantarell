Summary:	Cantarell fonts
Summary(pl.UTF-8):	Fonty Cantarell
Name:		fonts-OTF-Cantarell
Version:	0.0.9
Release:	2
License:	OFL v1.1
Group:		Fonts
Source0:	http://ftp.gnome.org/pub/GNOME/sources/cantarell-fonts/0.0/cantarell-fonts-%{version}.tar.xz
# Source0-md5:	606275190e4c1927ce4b4cfdb55363a2
URL:		http://abattis.org/cantarell/
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_otffontsdir	%{_fontsdir}/OTF

%description
Cantarell is a set of fonts designed by Dave Crossland. It is a
sans-serif Humanist typeface family.

%description -l pl.UTF-8
Cantarell to zbiór fontów zaprojektowanych przez Dave'a Crosslanda.
Jest to rodzina krojów bezszeryfowych Humanist.

%prep
%setup -q -n cantarell-fonts-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_otffontsdir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.avail
install -d $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

cp -a otf/*.otf $RPM_BUILD_ROOT%{_otffontsdir}
cp fontconfig/31-cantarell.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.avail
ln -s ../conf.avail/31-cantarell.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst OTF

%postun
fontpostinst OTF

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README
%{_sysconfdir}/fonts/conf.avail/31-cantarell.conf
%{_sysconfdir}/fonts/conf.d/31-cantarell.conf
%{_otffontsdir}/Cantarell-*.otf
