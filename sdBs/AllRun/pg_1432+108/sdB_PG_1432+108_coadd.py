from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[218.809833,10.608608],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1432+108/sdB_PG_1432+108_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1432+108/sdB_PG_1432+108_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
