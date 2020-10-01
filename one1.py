for iii in range(int(input())):    
    n,l = map(int, input().split())
    a = [0 for _ in range(n+3)]
    
    a[0] = 0
    a[n+1] = l
    
    left = [[0.0, 0.0] for _ in range(n+3)]
    right = [[0.0, 0.0] for _ in range(n+3)]
    
    left[0][0] = 1.0;
    left[0][1] = 0;
    
    right[n+1][0] = 1.0;
    right[n+1][1] = 0;
    
    a[1:n+1] = list(map(int, input().split()))
        
    for i in range(1, n+1):
        left[i][0] = left[i-1][0] + 1;
        left[i][1] = left[i-1][1] + (1.0*(a[i] - a[i-1]))/left[i-1][0];
    
    for i in range(n, 0, -1):
        right[i][0] = right[i+1][0] + 1;
        right[i][1] = right[i+1][1] + (1.0 * (a[i+1] - a[i]))/right[i+1][0]
        
    ans = -1
    for i in range(1, n+2):
        tl = left[i-1][1]
        tr = right[i][1]
        
        sl = left[i-1][0]
        sr = right[i][0]
        
        dl = a[i-1]
        dr = a[i]
        
        if tl < tr:
            dl += sl*(tr - tl)
        
        if tr < tl:
            dr -= sr*(tl - tr)
            
        ans = max(tl, tr)
        
        if dl <= dr:
            cs = (sl + sr)
            dis = (dr - dl)
            
            ans = ans + (1.0*dis/cs)
            break
        
    print(ans)
    
#     	for(lli i = 1; i<=n+1; i++)
# 		{
# 			double tl = left[i-1][1];
# 			double tr = right[i][1];

# 			double sl = left[i-1][0];
# 			double sr = right[i][0];

# 			double dl = a[i-1];
# 			double dr = a[i];

# 			if(tl < tr)
# 			dl += sl*(tr - tl);

# 			if(tr < tl)
# 			dr -= sr*(tl-tr);

# 			ans = max(tl, tr);
			
# 			if(dl <= dr)
# 			{
# 				double cs = (sl + sr);
# 				double dis = (dr - dl);
# 				ans = ans + ((1.0 * dis)/cs);
# 				break;
# 			}
# 		}
