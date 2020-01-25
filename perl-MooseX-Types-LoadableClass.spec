#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	MooseX
%define		pnam	Types-LoadableClass
Summary:	MooseX::Types::LoadableClass - ClassName type constraint with coercion to load the class
Name:		perl-MooseX-Types-LoadableClass
Version:	0.006
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f5cf26d8f6bae56195ff5dec848351e8
URL:		http://search.cpan.org/dist/MooseX-Types-LoadableClass/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Load >= 0.06
BuildRequires:	perl-Moose
BuildRequires:	perl-MooseX-Types >= 0.22
BuildRequires:	perl-namespace-clean
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
    use Moose::Util::TypeConstraints;

    my $tc = subtype as ClassName;
    coerce $tc, from Str, via { Class::MOP::load_class($_); $_ };

I've written those three lines of code quite a lot of times, in quite
a lot of places.

Now I don't have to.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MooseX/Types/LoadableClass.pm
%{_mandir}/man3/*
