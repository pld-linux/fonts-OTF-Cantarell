Summary:	Cantarell fonts
Summary(pl.UTF-8):	Fonty Cantarell
Name:		fonts-OTF-Cantarell
Version:	0.0.17
Release:	1
License:	OFL v1.1
Group:		Fonts
Source0:	http://ftp.gnome.org/pub/GNOME/sources/cantarell-fonts/0.0/cantarell-fonts-%{version}.tar.xz
# Source0-md5:	388bd4d11908c08ebe5ad6100ecf0819
URL:		http://abattis.org/cantarell/
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	fontpostinst
Requires:	fontconfig >= 1:2.10.1
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
install -d $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail
install -d $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

cp -a otf/*.otf $RPM_BUILD_ROOT%{_otffontsdir}
cp fontconfig/31-cantarell.conf $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail
ln -s %{_datadir}/fontconfig/conf.avail/31-cantarell.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst OTF

%postun
fontpostinst OTF

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README
%{_datadir}/fontconfig/conf.avail/31-cantarell.conf
%{_sysconfdir}/fonts/conf.d/31-cantarell.conf
%{_otffontsdir}/Cantarell-*.otf
