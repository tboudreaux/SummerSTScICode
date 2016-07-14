from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[312.286958,-20.501619],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_bps_cs22880-78/sdB_bps_cs22880-78_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_bps_cs22880-78/sdB_bps_cs22880-78_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
