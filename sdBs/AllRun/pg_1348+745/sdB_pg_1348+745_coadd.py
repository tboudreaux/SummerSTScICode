from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[207.181667,74.262917],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1348+745/sdB_pg_1348+745_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1348+745/sdB_pg_1348+745_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
