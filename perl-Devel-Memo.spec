#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	Memo
Summary:	Devel::Memo - memoize function calls
Summary(pl):	Devel::Memo - zapamiêtuj±cy wywo³ania funkcji
Name:		perl-Devel-Memo
Version:	0.004
Release:	10
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_with_tests:1}%{!?_with_tests:0}
BuildRequires:	perl-FreezeThaw
BuildRequires:	perl-Test-Helper
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::Memo permits you to create function objects (i.e. blessed
code-refs which can be bound to subroutine cells) which are called
exactly like a regular subroutine (which you supply), but which
memoize their arguments and results with each invocation, so that
unnecessary recomputation is avoided. Internally, the FreezeThaw
module is used to assist in the caching.

%description -l pl
Modu³ Devel::Memo umo¿liwia tworzenie obiektów funkcji (czyli
pob³ogos³awionych code-refs, które mog± byæ przypisane do komórek
procedur), które s± wywo³ywane dok³adnie tak jak normalne procedury
(które siê podaje), ale przy ka¿dym wywo³aniu zapamiêtuj± parametry i
wyniki, zapobiegaj±c niepotrzebnym ponownym obliczeniom. Wewnêtrznie
u¿ywany jest modu³ FreezeThaw, pomagaj±cy przy buforowaniu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO CHANGES
%{perl_sitelib}/Devel/Memo.pm
%{_mandir}/man3/*
