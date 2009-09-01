Summary:	freedesktop.org menu and desktop files specifications support for the awesome window manager
Summary(hu.UTF-8):	freedesktop.org menü és desktop fájlok támogatása az awesome ablakkezelőhöz
Summary(pl.UTF-8):	Obsługa menu i plików desktop zgodnych ze specyfikacją freedesktop.org
Name:		awesome-plugin-freedesktop
Version:	20090628
Release:	1
License:	GPL v2
Group:		X11/Window Managers/Tools
URL:		http://github.com/terceiro/awesome-freedesktop/tree/master
## git clone git://github.com/terceiro/awesome-freedesktop.git
Source0:	http://carme.pld-linux.org/~uzsolt/sources/awesome-freedesktop-%{version}.tar.bz2
# Source0-md5:	274bd2c8fcd906a8fb6570b6557ca65b
Requires:	awesome-plugin-awful
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project aims to add support for freedesktop.org compliant desktop
entries and menu. Main features:
- a freedesktop.org-compliant (or almost) applications menu
- a freedesktop.org-compliant (or almost) desktop
- a (yet limited) icon lookup function.

%description -l hu.UTF-8
Ez a project menübe szervezi a freedesktop.org desktop-bejegyzéseit.
Fő lehetőségek:
- freedesktop.org alkalmazás-menü
- freedesktop.org asztal
- egy (még korlátozott) ikon-keresési funkció.

%description -l pl.UTF-8
Biblioteka lua dla awesome, która pozwala w konfiguracji awesome dodać obsługę:
- menu aplikacji zgodne z freedesktop.org
- plików desktop zgodnych z freedesktop
- wyszukiwania ikon.

%prep
%setup -q -n awesome-freedesktop

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/awesome/lib/freedesktop
cp freedesktop/* $RPM_BUILD_ROOT%{_datadir}/awesome/lib/freedesktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO awesome-freedesktop.png
%{_datadir}/awesome/lib/freedesktop
