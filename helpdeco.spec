Summary:	Utility program to dissect Windows help files
Summary(de):	Utility-Programm zum Zerlegen von Windows Hilfedateien
Summary(pl):	Narzêdzie do rozk³adania windowsowych plików pomocy
Name:		helpdeco
Version:	2.1
Release:	2
License:	Freeware (non-commercial use and distribution only)
Group:		Applications/File
Source0:	http://www.helpmaster.com/zip/helpdc21.zip
# Source0-md5:	a5f9ceca5bb348aebb6a422f4941dad8
Patch0:		%{name}-linux-port.patch
URL:		http://www.helpmaster.com/hlp-developmentaids-helpdeco.htm
BuildRequires:	unzip
# no x86 asm, but requires 16-bit short, 32-bit long and little-endian CPU
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		__unzip		unzip -q -L

%description
HELPDECO dissects HLP help files of Windows 3.0, 3.1, 3.11, and 95 and
many MVB multi media viewer titles into all files required for a
rebuild using the appropriate help compiler HC30, HC31, HCP, HCW,
HCRTF, WMVC, MMVC or MVC.

%description -l de
HELPDECO zerlegt HLP-Hilfedateien von Windows 3.0, 3.1, 3.11 und 95
und viele MVB-Dateien des Multimedia-Viewers in alle für den
jeweiligen Hilfecompiler HC30, HC31, HCP, HCW, HCRTF, WMVC, MMVC oder
MVC zum erneuten Zusammenbau erforderlichen Dateien.

%description -l pl
HELPDECO rozk³ada pliki HLP z Windows 3.0, 3.1, 3.11 i 95 oraz wiele
rodzajów plików MVB na wszystkie pliki potrzebne do przebudowania przy
u¿yciu odpowiedniego kompilatora (HC30, HC31, HCP, HCW, HCRTF, WMVC,
MMVC lub MVC).

%prep
%setup -q -c
%patch -p1

%build

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install splitmrb zapres helpdeco $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc helpdeco.txt helpfile.txt
%attr(755,root,root) %{_bindir}/*
