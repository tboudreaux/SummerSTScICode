from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[13.320375,22.494253],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_0050+222/sdB_pg_0050+222_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_0050+222/sdB_pg_0050+222_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
