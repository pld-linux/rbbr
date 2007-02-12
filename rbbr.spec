Summary:	Ruby Class Browser
Summary(pl.UTF-8):	Przeglądarka klas dla Ruby
Name:		rbbr
Version:	0.6.0
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/ruby-gnome2/%{name}-%{version}-withapi.tar.gz
# Source0-md5:	2cb0648b87590db04d702f7fd26f8c8f
URL:		http://ruby-gnome2.sourceforge.jp/hiki.cgi?rbbr
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
Requires:	ruby-gnome2
BuildArch:	noarch
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class Browser written in Ruby with Gnome2.

%description -l pl.UTF-8
Przeglądarka klas napisana w języku Ruby z użyciem Gnome2.

%prep
%setup -q -n %{name}-%{version}-withapi

%build
ruby install.rb config \
	--std-ruby=%{ruby_rubylibdir} \
	--site-ruby=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

ruby install.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{_bindir}}

ruby install.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.ja ChangeLog
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/*.rb
%{ruby_rubylibdir}/%{name}
%{_datadir}/%{name}
