from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[320.983917,-19.014906],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_bps_cs29506-31/sdB_bps_cs29506-31_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_bps_cs29506-31/sdB_bps_cs29506-31_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
