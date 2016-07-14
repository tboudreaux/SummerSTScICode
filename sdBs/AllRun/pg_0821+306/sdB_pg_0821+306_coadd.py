from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[126.141875,30.481833],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_0821+306/sdB_pg_0821+306_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_0821+306/sdB_pg_0821+306_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
