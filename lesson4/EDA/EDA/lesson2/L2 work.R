reddit<- read.csv('reddit.csv')
reddit

table(reddit$employment.status)
summary(reddit)
str(reddit)


install.packages('ggplot2',dependencies = T)
library(ggplot2) 

new_age<-c("Under 18","18-24","25-34" , "35-44" , "45-54","55-64", "65 or Above")
new_age2<-c("65 or Above","Under 18","18-24","25-34" , "35-44" , "45-54","55-64")
reddit$age.range<-ordered(reddit$age.range,levels=new_age)
reddit$age.range<-factor(reddit$age.range,levels=new_age2,ordered = F)

levels(reddit$age.range)

qplot(data=reddit,x=age.range)
library(ggplot2)
pf <- read.csv('pseudo_facebook.tsv', sep = '\t')
names(pf)

qplot(aes(x = dob_day),data = pf) +
  geom_bar()+
  scale_x_discrete(breaks=1:31)+
  facet_wrap(~dob_month, ncol =3)

ggplot(aes(x = dob_day), data = pf)+
  geom_histogram(binwidth = 1)+
  scale_x_continuous(breaks = 1:31)

qplot(data = reddit,x=income.range)
levels(reddit$income.range)
new_income<-c("Under $20,000","$20,000 - $29,999" ,"$30,000 - $39,999" ,"$40,000 - $49,999","$50,000 - $69,999","$70,000 - $99,999","$100,000 - $149,999","$150,000 or more")
reddit$income.range<-ordered(reddit$income.range,levels=new_income)
