%global tl_name iwona
%global tl_revision 77682
%global tl_version 0.995b

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	A two-element sans-serif font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/iwona
License:	gfl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/iwona.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/iwona.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Iwona is a two-element sans-serif typeface. It was created as an
alternative version of the Kurier typeface, which was designed in 1975
for a diploma in typeface design at the Warsaw Academy of Fine Arts
under the supervision of Roman Tomaszewski. This distribution contains a
significantly extended set of characters covering the following modern
alphabets: latin (including Vietnamese), Cyrillic and Greek as well as a
number of additional symbols (including mathematical symbols). The fonts
are prepared in Type 1 and OpenType formats. For use with TeX the
following encoding files have been prepared: T1 (ec), T2 (abc), and OT2
--Cyrillic, T5 (Vietnamese), OT4, QX, texansi and nonstandard (IL2 for
the Czech fonts), as well as supporting macros and files defining fonts
for LaTeX.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from iwona:
Map iwona.map
TL_DROPIN_EOF
