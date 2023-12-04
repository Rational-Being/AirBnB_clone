#!/usr/bin/env bash
{
	cat <<-'EOH'
EOH
echo
git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf
} > AUTHORS
