# Run tests in check section
# Disabled because it needs an ACCOUNT_NAME and ACCOUNT_KEY
%bcond_with check

# https://github.com/Azure/azure-storage-blob-go
%global goipath         github.com/Azure/azure-storage-blob-go
Version:                0.2.0

%global common_description %{expand:
The Microsoft Azure Storage SDK for Go allows you to build applications 
that takes advantage of Azure's scalable cloud storage.

This repository contains the open source Blob SDK for Go.

Features:

Blob Storage:
 - Create/List/Delete Containers
 - Create/Read/List/Update/Delete Block Blobs
 - Create/Read/List/Update/Delete Page Blobs
 - Create/Read/List/Update/Delete Append Blobs}

%gometa

Name:           %{goname}
Release:        0.1%{?dist}
Summary:        Microsoft Azure Blob Storage Library for Go
License:        MIT
URL:            %{gourl}
Source0:        %{gourl}/archive/%{version}/%{name}-%{version}.tar.gz

Patch0:         0001-Fix-unknown-field-MinimumLevelToLog-error.patch

BuildRequires: golang(github.com/Azure/azure-pipeline-go/pipeline)
BuildRequires: golang(gopkg.in/check.v1)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup -p1


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Oct 05 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-1
- First package for Fedora

