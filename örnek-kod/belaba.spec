Name:           belaba
Version:        0.1
Release:        1%{?dist}
Summary:        Bash ile Yazılmış Bir Merhaba Dünya örneği

License:        GPLv3+
URL:            https://www.example.com/%{name}
Source0:        https://www.example.com/%{name}/releases/%{name}-%{version}.tar.gz

Requires:       bash

BuildArch:      noarch

%description
Bash ile yazılmış Merhaba Dünya örneği için 
satırlara sığmayan
epey uzun bir 
tanıtım yazısı

%prep
%setup -q

%build

%install

mkdir -p %{buildroot}/%{_bindir}

install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}


%changelog
* Tue Sep 1 2020 Emrecan Şuşter <emrecansuster@lilyum.org> - 0.1-1
- Türkçeleştirildi. 
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org> - 0.1-1
- First bello package
