Summary:	LXQt standard themes
Summary(pl.UTF-8):	Standardowe motywy LXQt
Name:		lxqt-themes
Version:	2.4.0
Release:	1
License:	LGPL-2.0-or-later
URL:		https://lxqt-project.org/
Source0:	https://github.com/lxqt/lxqt-themes/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	5f7a80bc279fc8063ecd077653f3731b
BuildRequires:	lxqt-build-tools >= 2.4.0
BuildRequires:	perl-base
Requires:	breeze-cursor-theme
Requires:	hicolor-icon-theme
Requires:	kf6-breeze-icons
Requires:	kf6-breeze-icons-data
BuildArch:	noarch

%description
This package contains the standard themes for the LXQt desktop, namely
ambiance, Arch-Colors, Clearlooks, dark, frost, graphite, KDE-Plasma,
kvantum, Leech, light, silver, system, Valendas

%description -l pl.UTF-8
Ten pakiet zawiera standardowe motywy dla pulpitu LXQt, mianowicie:
ambiance, Arch-Colors, Clearlooks, dark, frost, graphite, KDE-Plasma,
kvantum, Leech, light, silver, system, Valendas

%prep
%setup -q

%build
%cmake -B build
%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%doc AUTHORS CHANGELOG README.md
%{_datadir}/lxqt/graphics
%dir %{_datadir}/lxqt/themes
%{_datadir}/lxqt/themes/{ambiance,Arch-Colors,Clearlooks,dark,frost,graphite,KDE-Plasma,kvantum,Leech,light,silver,system,Valendas}
%{_iconsdir}/hicolor/scalable/*/*.svg
%{_datadir}/lxqt/palettes
%{_datadir}/lxqt/wallpapers

%clean
rm -rf $RPM_BUILD_ROOT
