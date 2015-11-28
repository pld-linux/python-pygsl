%define 	module	pygsl
%define     snap    20080429
Summary:	Python interface to GSL
Summary(pl.UTF-8):	Pythonowy interfejs do GSL
Name:		python-%{module}
Version:	0.9.1
Release:	0.%{snap}
License:	GPL v2
Group:		Development/Languages/Python
#Source0:	http://dl.sourceforge.net/pygsl/%{module}-%{version}.tar.gz
Source0:    %{module}-%{snap}.tar.bz2
# Source0-md5:	c5851a4feeb991bf2ffb58e5b5fcd0ab
URL:		http://pygsl.sourceforge.net
Patch0:     %{name}-initmodule.patch
BuildRequires:  gcc
BuildRequires:  gsl-devel >= 1.11
BuildRequires:  python-numpy-devel >= 1.0.4
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python interface to GSL.

%description -l pl.UTF-8
Pythonowy interfejs do GSL.

%prep
%setup -q -n %{module}-%{snap}
%patch0 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog README TODO
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/*.so
%{py_sitedir}/%{module}/gsl_dist
%dir %{py_sitedir}/%{module}/statistics
%{py_sitedir}/%{module}/statistics/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/statistics/*.so
%dir %{py_sitedir}/%{module}/testing
%{py_sitedir}/%{module}/testing/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/testing/*.so
%{py_sitedir}/%{module}-*.egg-info
%{_includedir}/python*/pygsl
