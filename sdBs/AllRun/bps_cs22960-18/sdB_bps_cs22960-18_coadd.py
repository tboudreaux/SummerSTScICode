from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[332.104208,-43.200392],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_bps_cs22960-18/sdB_bps_cs22960-18_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_bps_cs22960-18/sdB_bps_cs22960-18_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()