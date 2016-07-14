from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[321.228667,15.984331],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_2122+157/sdB_PG_2122+157_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_2122+157/sdB_PG_2122+157_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()