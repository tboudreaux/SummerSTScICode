from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[325.2025,-1.035444],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_214048.60-010207.6/sdB_SDSSJ910_214048.60-010207.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_214048.60-010207.6/sdB_SDSSJ910_214048.60-010207.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
