Name:           celaba
Version:        1.0
Release:        1%{?dist}
Summary:        C ile Yazılmış Bir Merhaba Dünya örneği

License:        GPLv3+
URL:            https://www.example.com/%{name}
Source0:        https://www.example.com/%{name}/releases/%{name}-%{version}.tar.gz

Patch0:         celaba-ciktisi-ilk-yama.patch

BuildRequires:  gcc
BuildRequires:  make

%description
C ile yazılmış Merhaba Dünya örneği için 
satırlara sığmayan
epey uzun bir 
tanıtım yazısı

%prep
%setup -q

%patch0

%build
make %{?_smp_mflags}

%install
%make_install


%files
%license LICENSE
%{_bindir}/%{name}


%changelog
* Tue May 31 2016 Adam Miller <maxamillion@gmail.com> - 1.0-1
- İlk celaba paketi
