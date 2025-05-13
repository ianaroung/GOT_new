n = 381 # number of lists in taxonomy

def get_corelevance_matrix(relevance_matrix):
    for i in range(n):
        for j in range(n):
            T, T1, T2 = 0, 0, 0
            for k in range(relevance_matrix):                
                if relevance_matrix[i][k] >= 0.3 and relevance_matrix[j][k] >= 0.3: T += 1
                if relevance_matrix[i][k] >= 0.3: T1 += 1
                if relevance_matrix[j][k] >= 0.3: T2 += 1
            T = float(T)
            T1 = float(T1)
            T2 = float(T2)
            if T1 == 0 or T2 == 0: cor_kulch[i][j]= 0
            else: cor1_kulch[i][j]= T*(1/T1+1/T2)/2

    for i in range(n):
        for j in range(n):
            sum_i = 0
            sum_j = 0
            sum_min = 0
            for k in range(relevance_matrix):
                sum_min += relevance_matrix[i][k]*relevance_matrix[j][k]
                sum_i += relevance_matrix[i][k]
                sum_j += relevance_matrix[j][k]
    
            sum_min = float(sum_min)
            sum_i = float(sum_i)
            sum_j = float(sum_j)
            if sum_i == 0 or sum_j == 0:
                cor_mod_kulch[i][j]= 0
            else:
                cor_mod_kulch[i][j]= (sum_min/sum_i + sum_min/sum_j)/2
              
    for i in range(n):
    for j in range(n):
            sum_ij = 0
            for k in range(relevance_matrix):
                if n1_k[k] != 0:
                    sum_ij += relevance_matrix[i][k]*relevance_matrix[j][k]/23294/n1_k[k]
            sum_ij = float(sum_ij)
            cor_scalar[i][j]= sum_ij
      
    return cor_kulch, cor_mod_kulch, cor_scalar
