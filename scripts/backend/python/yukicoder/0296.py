n,h,m,t = map(int,input().split())

mod_h,mod_m = 24,60
add_h,add_m = divmod(t*(n-1),mod_m)

print((h + add_h + (m+add_m)//mod_m)%mod_h)
print((m+add_m)%mod_m)