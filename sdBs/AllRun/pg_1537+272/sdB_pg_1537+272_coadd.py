from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[234.909167,27.101783],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1537+272/sdB_pg_1537+272_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1537+272/sdB_pg_1537+272_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
