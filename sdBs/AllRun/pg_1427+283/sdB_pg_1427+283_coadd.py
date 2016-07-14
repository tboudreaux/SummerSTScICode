from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[217.496708,28.059467],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1427+283/sdB_pg_1427+283_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1427+283/sdB_pg_1427+283_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
