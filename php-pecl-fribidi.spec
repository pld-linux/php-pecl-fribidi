%define		php_name	php%{?php_suffix}
%define		modname	fribidi
%define		status		stable
Summary:	%{modname} - Implementation of the Unicode BiDi algorithm
Summary(pl.UTF-8):	%{modname} - Implementacja algorytmu BiDi Unicode
Name:		%{php_name}-pecl-%{modname}
Version:	1.0
Release:	7
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	360e55f049cdebc96fe797eba78399ef
Patch0:		php-pecl-%{modname}-new_fribidi.patch
URL:		http://pecl.php.net/package/fribidi/
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	fribidi-devel >= 0.10.9
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php(core) >= 5.0.4
Obsoletes:	php-fribidi
Obsoletes:	php-pear-%{modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A PHP frontend to the FriBidi library: an implemntation of the unicode
Bidi algorithm, provides means of handling right-to-left text.

In PECL status of this package is: %{status}.

%description -l pl.UTF-8
Frontend PHP do biblioteki FriBidi: implementacji algorytmu unicode
Bidi, dostarczającego środki do obsługi tekstu pisanego od prawej do
lewej.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .
%patch0 -p2

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
