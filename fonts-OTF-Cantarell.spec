Summary:	Cantarell fonts
Name:		fonts-OTF-Cantarell
Version:	0.0.7
Release:	1
License:	OFL
Group:		Fonts
Source0:	http://ftp.gnome.org/pub/GNOME/sources/cantarell-fonts/0.0/cantarell-fonts-%{version}.tar.xz
# Source0-md5:	5810bfe16ca46c26974d0058532f2b50
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
%doc NEWS README
%{_sysconfdir}/fonts/conf.avail/31-cantarell.conf
%{_sysconfdir}/fonts/conf.d/31-cantarell.conf
%{_otffontsdir}/*.otf
