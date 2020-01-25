#
# Conditional build:
%bcond_with	tests	# perform "make test"

%define		pdir	Devel
%define		pnam	Memo
Summary:	Devel::Memo - memoize function calls
Summary(pl.UTF-8):	Devel::Memo - zapamiętujący wywołania funkcji
Name:		perl-Devel-Memo
Version:	0.004
Release:	13
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8bb2fee3416368db795555feee4261a8
URL:		http://search.cpan.org/dist/Devel-Memo/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-FreezeThaw
BuildRequires:	perl-Test-Helper
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::Memo permits you to create function objects (i.e. blessed
code-refs which can be bound to subroutine cells) which are called
exactly like a regular subroutine (which you supply), but which
memoize their arguments and results with each invocation, so that
unnecessary recomputation is avoided. Internally, the FreezeThaw
module is used to assist in the caching.

%description -l pl.UTF-8
Moduł Devel::Memo umożliwia tworzenie obiektów funkcji (czyli
pobłogosławionych code-refs, które mogą być przypisane do komórek
procedur), które są wywoływane dokładnie tak jak normalne procedury
(które się podaje), ale przy każdym wywołaniu zapamiętują parametry i
wyniki, zapobiegając niepotrzebnym ponownym obliczeniom. Wewnętrznie
używany jest moduł FreezeThaw, pomagający przy buforowaniu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO CHANGES
%{perl_vendorlib}/Devel/Memo.pm
%{_mandir}/man3/*
