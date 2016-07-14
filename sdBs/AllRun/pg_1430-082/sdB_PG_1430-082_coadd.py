from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[218.4035,-8.472994],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1430-082/sdB_PG_1430-082_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1430-082/sdB_PG_1430-082_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
