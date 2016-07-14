from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[251.599708,34.768889],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_164623.93+344608.0/sdB_sdssj_164623.93+344608.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_164623.93+344608.0/sdB_sdssj_164623.93+344608.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
