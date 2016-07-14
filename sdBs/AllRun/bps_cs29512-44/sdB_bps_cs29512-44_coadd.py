from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[334.113125,-11.509983],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_bps_cs29512-44/sdB_bps_cs29512-44_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_bps_cs29512-44/sdB_bps_cs29512-44_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
