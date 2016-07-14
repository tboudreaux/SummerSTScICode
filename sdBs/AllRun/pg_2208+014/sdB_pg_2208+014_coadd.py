from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[332.689417,1.693167],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_2208+014/sdB_pg_2208+014_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_2208+014/sdB_pg_2208+014_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
