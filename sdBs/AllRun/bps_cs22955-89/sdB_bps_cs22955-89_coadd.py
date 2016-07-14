from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[306.930292,-27.010828],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_bps_cs22955-89/sdB_bps_cs22955-89_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_bps_cs22955-89/sdB_bps_cs22955-89_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
