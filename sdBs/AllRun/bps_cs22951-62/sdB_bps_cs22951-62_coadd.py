from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[327.678167,-43.674542],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_bps_cs22951-62/sdB_bps_cs22951-62_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_bps_cs22951-62/sdB_bps_cs22951-62_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
