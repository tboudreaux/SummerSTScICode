from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[142.127292,56.303403],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_0924+565/sdB_pg_0924+565_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_0924+565/sdB_pg_0924+565_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
