#!/bin/bash
/opt/yottadb/current/ydb << "EOF"
S ^IKNOW("text","After discussing his nausea, the patient didn't report suffering from chest pain, shortness of breath or tickling")=""
S ^IKNOW("text","I liked the striped pijamas, but the slippers didn't really fit with it")=""
S ^IKNOW("text","Upon exam two weeks ago the patient's weight was 146.5 pounds")=""
EOF
chmod +x /tmp/run.sh
/tmp/run.sh
