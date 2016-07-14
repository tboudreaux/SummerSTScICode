from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[124.033083,48.063842],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_0812+482/sdB_pg_0812+482_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_0812+482/sdB_pg_0812+482_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
