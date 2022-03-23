fastapitoken: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

# end-points
1]courses:
    GET:
     /active: returns all courses which are present with content.
     /all: returns all courses which are present with or without content.

    POST:
    
2]results:
    GET:
     /
     /cleared: candidates who cleared all the tests and eligible for certificate.
     /notclear: candidates who not cleared all the tests and not eligible for certificate.
     

    POST:
     /update/{sec_name}/{user_id}: updates the section result of candidates
     /flush/{sec_name}/{user_id}: set the section result to zero

3] users:
    GET:
     


