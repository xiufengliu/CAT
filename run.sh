export OTREE_ADMIN_PASSWORD=Abcd1234#
export OTREE_PRODUCTION=0 # uncomment this line to enable production mode

#export OTREE_AUTH_LEVEL=STUDY #STUDY DEMO
export OTREE_AUTH_LEVEL=DEMO
#export DATABASE_URL=postgres://xiuli:Abcd1234@postgresql:5432/otree
#export DATABASE_URL=sqlite:////home/xiuli/PycharmProjects/CAT/db.sqlite3

#export DATABASE_URL=sqlite:////opt/CAT/db.sqlite3
#otree resetdb

#otree prodserver 8080

otree devserver 8080
#otree runserver -v 3 8080