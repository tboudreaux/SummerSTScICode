from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[326.550708,0.852778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_214612.17+005110.0/sdB_sdssj9-10_214612.17+005110.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_214612.17+005110.0/sdB_sdssj9-10_214612.17+005110.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
